
# PySpark Streaming Example

## Setup Instructions

### Prerequisites

- Python installed on your system (Python 3.x recommended).
- Apache Spark installed and configured (with `SPARK_HOME` set).
- Basic understanding of Python and streaming concepts.

### Installation

```sh
pip install pyspark
```

### Running the Example

#### Step-by-Step Guide

1. **Start the TCP Listener:**

   ```sh
   cd path\to\netcat
   nc -lk 9999
   ```

2. **Run the PySpark Streaming Script:**

   ```sh
   python .\pyspark_streaming.py
   ```

3. **Send Data Using Netcat:**

   ```sh
   nc localhost 9999
   ```

4. **View the Output:**

   - **Console Output:**
   
     ```
     -------------------------------------------
     Time: 2024-06-19 12:34:56
     -------------------------------------------
     ('hello', 1)
     ('world', 1)
     ('spark', 1)
     ('streaming', 1)
     ('example', 1)
     ('apache', 1)
     ('is', 1)
     ('awesome', 1)
     ```

   - **Text Files:**

     The word counts will be saved to text files in the `output/word_counts` directory.
```

