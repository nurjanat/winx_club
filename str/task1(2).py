mails = ['hello sophie how are you',
         'hello pls help me!!!',
         'Sophie, production is dows go to work!!!',
         'sophie, i need your help',
         'SOS!!! come to work pls',
         'good night, Sophie',
         'SALES!Lining lala',
         'Nikes China Buy right now',
         'HeLP Sophie',
         'Hey sophie how are you',
         'Please come with me'
        ]





def delete(mails_list:list):
    for sentence in mails_list:
        sentence = sentence.lower()
        if 'help' in sentence or 'urgent' in sentence or 'sos' in sentence:
            with open('spam.txt','a') as f1:
                f1.write(sentence)
        elif sentence.startswith('sales') or 'buy right now' in sentence or sentence.endswith("!!!"):
            with open('spam.txt','a') as f2:
                f2.write(sentence)
        else:
            with open('mail.txt','a') as f3:
                f3.write(sentence)
delete(mails)
