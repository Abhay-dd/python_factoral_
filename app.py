from flask import Flask,render_template,request 

app = Flask(__name__) #name theh 

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def hi():
    if request.method=='POST':
        num1=request.form['num1']
        output = fact(int(num1)) #calling function
    return render_template('result.html',num1=num1,output=output)# just type num1=num1,output=output

def fact(num1):#this is the fuction to printing factoral 
  m=1
  for x in range(1,num1+1):
    m=m*x
  return(m)



if __name__=='__main__':# this two lines are output line
    app.run()