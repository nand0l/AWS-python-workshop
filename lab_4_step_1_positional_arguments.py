import boto3


def translate_text(
    text, source_language_code, target_language_code
):  # we define the positional arguments in the ()
    client = boto3.client("translate")
    response = client.translate_text(
        Text=text,  # we remove the hard coded value
        SourceLanguageCode=source_language_code,  # we used the positional argument instead
        TargetLanguageCode=target_language_code,
    )
    print(response)
    # from the response I only wat to print the Translated text output.
    print(response["TranslatedText"])


def main():
    translate_text(
        "I am learning to code in AWS", "en", "nl"
    )  # we provide the value for the arguments when we call the function in the correct positional order.


if __name__ == "__main__":
    main()
