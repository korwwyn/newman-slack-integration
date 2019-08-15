# newman-slack-integration

## Whay it was created?

Just because I have found no easy way to transfer data of newman runs to slack :man_shrugging:

## Requirements
```
node 8 +
python3.6
```
## Quick guide

1. Install newman

```bash
$ npm i -g newman
```
2. Install requirements for python

```bash
$ pip3 install -r requirements.txt
```

3. Obtain your [Slack API token](https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens)

4. In main.py file enter your Slack channel name

5. In run_all_collections.py file enter address to your environment (it could shared, as in example, or it can be a json file)

6. Run your API tests!
```bash
$ SLACK_API_TOKEN='YOUR_SLACK_API_TOKEN' python3 run_all_collections.py
```

## How it looks?

![example.png](http://i.imgur.com/2MlNn7w.png)