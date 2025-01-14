import boto3


def translate_text(**kwargs):
    client = boto3.client("translate")
    response = client.translate_text(**kwargs)
    print(response)
    # from the response I only wat to print the Translated text output.
    print(response["TranslatedText"])


### Change below this line only ###

kwargs = {
    "Text": "I am learning to code in AWS",
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "fr",
}


def main():
    translate_text(**kwargs)


if __name__ == "__main__":
    main()
