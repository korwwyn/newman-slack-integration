import os
import slack
import subprocess

newman_args='--reporters cli --reporter-cli-no-failures --reporter-cli-no-assertions --reporter-cli-no-success-assertions  --reporter-cli-no-console'
headers = {}

slack_channel = '#your_channel_name'
file_name = "console_log.txt"

def send_message(output):
    """
    Sends message with test results to Slack
    """
    client = slack.WebClient(token = os.environ['SLACK_API_TOKEN'])

    response = client.chat_postMessage(
        channel=slack_channel,
        text=("```%s```") % output
    )
    assert response["ok"]

def send_message_collection_start(collection_name, environment_name):
    """
    Sends message that collection started to Slack
    """
    client = slack.WebClient(token = os.environ['SLACK_API_TOKEN'])

    response = client.chat_postMessage(
        channel=slack_channel,
        text=("*%s* on *%s* started") % (collection_name, environment_name)
    )
    assert response["ok"]

def send_message_collections_finished():
    """
    Sends message that all collections finished to Slack
    """
    client = slack.WebClient(token = os.environ['SLACK_API_TOKEN'])

    response = client.chat_postMessage(
        channel=slack_channel,
        text=("*Collections run finished*")
    )
    assert response["ok"]

def get_collection_output():
    """
    Get slack-readable output for newman results
    """
    with open(file_name, "r", encoding = 'utf-8') as f:
        lines = f.readlines()
        report_lines = lines[-20:] # -> 20 - number of lines for results

    with open(file_name, "w") as f:
        for line in report_lines:
            f.write(line)

    f = open(file_name, "r")
    output = f.read()

    return output

def run_collection(collection, collection_name, environment, environment_name):
    send_message_collection_start(collection_name, environment_name)
    os.system('newman run %s -e %s %s > %s' % (collection, environment, newman_args, file_name))
    send_message(get_collection_output())

# run_collection(collection, environment)