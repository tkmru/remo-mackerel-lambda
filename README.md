# remo to mackerel
This code get my room temperature from Nature Remo, and post it as service metrics to mackerel by AWS Lambda.

## Usage

```
$ mkdir packages
$ cd packages/
$ pip install requests -t .
$ zip -r9 ../function.zip .
$ zip -g function.zip lambda_function.py
```

and upload function.zip to AWS Lambda.
