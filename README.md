# beehiveai-aws-collector
Service that collects aws data and sends it to beehive

## Configuration

```shell
BEEHIVEAI_CHECK_INTERVAL=xxx
BHIVE_API_TOKEN=xxx
```
BHIVE_API_TOKEN
* The token used for connecting to Beehive AI API

BEEHIVEAI_CHECK_INTERVAL
* How often information from aws services is gathered

## Running

```shell
docker-compose up
```

## License
[Apache 2](http://www.apache.org/licenses/LICENSE-2.0)