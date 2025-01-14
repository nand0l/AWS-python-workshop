import boto3

client = boto3.client("translate")


def translate_text():
    response = client.translate_text(
        Text="I am learning to code in AWS",
        SourceLanguageCode="en",
        TargetLanguageCode="fr",
    )
    print(
        response
    )  # this code is inside the function and will print the contents of the variable 'response'
    # from the response I only wat to print the Translated text output.
    print(response["TranslatedText"])


def main():
    translate_text()


if __name__ == "__main__":
    main()
