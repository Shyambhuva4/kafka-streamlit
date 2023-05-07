Open a terminal and start the Kafka cluster: docker-compose up -d

Install the required python dependencies to run the scripts: python pip install -r requirements.txt
In a new terminal, launch the analyzer script: python analyzer.py
In a new terminal, launch the analysis consumer script: python analysis_consumer.py
In a new terminal, use the ts producer script to create time series and push them on the cluster: python ts_producer.py
In a new terminal, start streamlit: streamlit run app.py
