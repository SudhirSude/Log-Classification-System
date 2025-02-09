# Log-Classification-System

**Log Classification System**

**Overview**

The Log Classification System is an automated tool that categorizes log
messages using a combination of regular expressions, machine learning,
and large language models (LLMs). It processes logs from various sources
and applies a multi-step classification approach to assign meaningful
labels.

**Key Features**

-   **Regex-Based Classification**: Uses predefined patterns to classify
    well-known log formats quickly.

-   **BERT-Based Classification**: Generates embeddings for logs and
    applies a trained classifier when regex fails.

-   **LLM-Based Classification**: For specific sources (e.g.,
    \"LegacyCRM\"), an LLM is used to categorize logs when other methods
    are insufficient.

-   **CSV Processing**: Supports bulk log classification from CSV files.

-   **FastAPI Integration**: Provides a REST API endpoint for log
    classification via file upload.

**Technologies Used**

-   **Python**: Core programming language.

-   **Regex**: For pattern-based classification.

-   **BERT**: For semantic classification using pre-trained models.

-   **LLM (Groq API)**: For advanced classification using large language
    models.

-   **FastAPI**: For building the RESTful API.

-   **Pandas**: For handling CSV data.

![image](https://github.com/user-attachments/assets/a92ab905-cbf4-4d99-927c-594796048796)


**Step 1: Extract Log Data from Excel**

-   Load the log data from an Excel file.

-   Preprocess the logs by removing unnecessary characters, normalizing
    text, and handling missing values.

**Step 2: Generate Embeddings Using BERT/Sentence Transformer**

-   Convert each log message into a numerical representation using a
    **pre-trained BERT or Sentence Transformer**.

-   These embeddings capture semantic similarities between log messages.

**Step 3: Cluster Logs Using DBSCAN (Unsupervised Learning)**

-   Apply DBSCAN (Density-Based Spatial Clustering of Applications with
    Noise) to group similar logs.

-   Identify patterns within each cluster and analyze frequent log
    structures.

-   Use these clusters to derive regular expression (regex) patterns for
    common log types.

**Step 4: Build Regex-Based Classification**

-   Create regex rules based on clustered logs to classify known log
    patterns.

-   If a **new log matches a regex pattern**, it is assigned to a
    **valid class**.

-   If a **new log does not match any regex**, it is labeled as
    **Unknown** and needs further classification.

**Step 5: Classify Unknown Logs Using Machine Learning**

-   **Check if enough training samples are available for
    classification:**

    -   **If Yes:**

        -   Generate **BERT embeddings** for the new log.

        -   Apply **Logistic Regression** to classify the log into a
            known category.

    -   **If No:**

        -   Use an **LLM-based classification** for prediction (since a
            few-shot or zero-shot approach may work better for unseen
            logs).
