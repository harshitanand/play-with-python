import pyparsing as pp

questionspreamble = pp.Word(pp.alphanums + " \ \n") ("questionspreamble")
questionSectiontype = pp.Word(pp.alphas + " " + "\n")("questionSectiontype")
qno = pp.Word("\n"+pp.nums + ". ")("qno")
questioninfo = pp.Word(pp.alphanums + " ")("questioninfo")
opt = pp.Word("(" + pp.alphas +")")("opt")
answerinfo =pp.Word(pp.alphanums + " \." , pp.alphanums + " \." + "\n" + pp.alphanums)("answerinfo")

answer = pp.Group(opt + answerinfo)("answer")
answers = pp.Group(pp.OneOrMore(answer))("answers")

question = pp.Group(qno + questioninfo + answers)("question")
questionsection = pp.Group(questionSectiontype + pp.OneOrMore(question))("questionsection")

QuestionsDoc = pp.Group( questionsection)("QuestionDoc")

data = str(raw_input("Enter the path of file to convert : "))
data1 =str(raw_input("Enter the path of file to produce : ")) 
out = (QuestionsDoc.parseString(open(data).read()))
fp = open(data1, "w")
fp.write(out.asXML())

