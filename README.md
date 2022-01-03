# GetSeatGoLogging

This project aims to serve as the logging service for the GetSeatGo App

## Requirements

To run the service, create a virtual environment and install the requirements by running the following command:

```setup
pip install -r requirements.txt
```

## Usage

Either export the following **configurations** `environment variables` or set their values in config.json

- App Details Environment Variables
```usage
export "TITLE"="GetSeatGo",
export "VERSION"="0.0.1"
export "DESCRIPTION"="Logging Service for GetSeatGo App"
export "HOST"="0.0.0.0"
export "PORT"=8081
export "RELOAD"=true
export "DEBUG"=true # only in case of debugging, in production, it to false
```

- MongoDB Environment Variables
```usage
export MONGO_HOST=localhost
export MONGO_PORT=27017
export MONGO_URI=
export MONGO_ENV=PRODUCTION
export MONGO_USERNAME=
export MONGO_PASSWORD=
```

- RabbitMQ Environment Variables
```usage
export rabbitmq_username=guest
export rabbitmq_password=guest
export rabbitmq_host=localhost
export rabbitmq_port=15672
export rabbitmq_virtual_host=/
export rabbitmq_exchange=
export rabbitmq_exchange_type=
export rabbitmq_consumer_queue=
```

Start the service by running the following command in the outermost directory 
```usage
python main.py
```