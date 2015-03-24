Write a python command line script to analyze an input file containing exam questions and write the analyzed output to an XML file.
You have been given two sample inputs (.txt) and their corresponding sample outputs (.xml) to make the assignment more clear.

The input file will contain an optional exam heading (any text, e.g. 'Paper 1') followed by the question type, followed by one or more questions.
You can assume that currenty there is only a single question type, 'Single Correct Answer Type'.

Each question will begin on a new line, and contain the question number followed by a dot, then the question text, then up to four options (a/b/c/d).
The options will contain an option specification followed by the option text. 
The option specification can be of the format a) as in input1, or (a) as in input2.
Your program should be configurable at run-time to accept either of these formats.
Both question text and option text can span across multiple lines.
You can either delete newlines within text from the output, or retain them.

The input may contain multiple options on the same line.

The input file will be encoded in UTF-8, and may contain non-ASCII Unicode characters such as α.

Assuming the input meets this specification, the output of your program should be a valid XML file. 
The output XML filename will be the input filename with .txt replaced by .xml.
The XML file should capture the structure of the input, as shown in the sample output files. 
As you can see, the output XML format is identical for the two input formats.

In general, your program should be tolerant to white space, other than the specifications given above.
If the input does not meet the specifications, the output XML can be blank or skipped, but try and pinpoint the error and exit gracefully.