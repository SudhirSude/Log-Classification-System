import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse

from classify import classify

app = FastAPI()

# Define a FastAPI endpoint to classify logs
@app.post("/classify/")
async def classify_logs(file: UploadFile):
    # Validate the uploaded file type
    if not file.filename.endswith('.csv'):
        # Raise an error if the file is not a CSV
        raise HTTPException(status_code=400, detail="File must be a CSV.")
    
    try:
        # Read the uploaded CSV into a Pandas dataframe
        df = pd.read_csv(file.file)
        
        # Check if the required columns exist in the dataframe
        if "source" not in df.columns or "log_message" not in df.columns:
            # Raise an error if the required columns are missing
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns.")

        # Perform classification on the data
        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

        # Print the modified dataframe for debugging purposes
        print("Dataframe:", df.to_dict())

        # Save the modified dataframe to a new CSV file
        output_file = "resources/output.csv"
        df.to_csv(output_file, index=False)
        print("File saved to output.csv")
        
        # Return the saved CSV file as a response
        return FileResponse(output_file, media_type='text/csv')
    except Exception as e:
        # Raise a 500 error if any exception occurs during processing
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Close the uploaded file to free up resources
        file.file.close()
        # Clean up the saved file (commented out for now)
        # if os.path.exists("output.csv"):
        #     os.remove("output.csv")