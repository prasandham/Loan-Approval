import re 
from flask import Flask, render_template, url_for, request , redirect

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    class Loan:
        cred_score={"123456789":0,"111111111":0,"222222222":750,"333333333":880,"444444444":630}
        def __init__(self,loan_amt,tenure,income1,income2,expenses,ssn,workex,name,phone):
            self.loan_amt=loan_amt
            self.tenure=tenure
            self.income1=income1
            self.income2=income2
            self.expenses=expenses
            self.ssn=ssn
            self.workex=workex
            self.name=name
            self.phone=phone
        def incometest(self):
            fill_det=4
            if self.loan_amt=="" or self.tenure=="" or self.income1=="" or self.income2=="" or self.expenses=="" or self.ssn=="" or self.workex=="" or self.name=="" or self.phone=="":
                return fill_det
            else:
                try:
                    n=float(self.loan_amt)+float(self.income1)+float(self.income2,)+float(self.tenure)+float(self.expenses)+float(self.phone)+float(self.ssn)+float(self.workex) 
                except:
                    return fill_det
            self.phone=re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1)\2-\3',self.phone)
            incm1=float(self.income1)
            incm2=float(self.income2)
            incm=(incm1+incm2)/2
            r=0.04
            n=float(self.tenure)
            exp=float(self.expenses)
            p=float(self.loan_amt)
            emi=float(p*r*((1+r)**n))/(((1+r)**n)-1)
            foir=(emi+exp)/(incm/12)
            return self.approve(foir)

        def approve(self,foir):
            file=open("data.txt", "a")
            data_list=["\n",self.loan_amt, "\t", self.tenure,"\t", self.income1,"\t", self.income2, "\t",self.expenses, "\t",self.ssn, "\t",self.workex, "\t",self.name, "\t",self.phone]
            file.writelines(data_list)      
            file.close()  
            loan_accept1=1
            workex_reject1=2
            loan_reject1=3
            fill_det=4
            incm=0
            incm1=float(self.income1)
            incm2=float(self.income2)
            incm=(incm1+incm2)/2
            p=float(self.loan_amt)
            work_exp=float(self.workex)
            if str(self.ssn) in self.cred_score.keys():   
                if self.cred_score[str(self.ssn)]<700:
                    return loan_reject1
            elif incm<=30000 and foir>0.60:
                return loan_reject1   
            elif incm>30000 and incm<=100000  and foir>0.75:
                return loan_reject1
            elif (incm>100000) and foir>0.80:
                return loan_reject1
            elif work_exp<=1.5:
                return workex_reject1
            else:
                return loan_accept1

    if request.method=="POST":
        loan_amt=request.form["loan_amt"]
        tenure=request.form["tenure"]
        income1=request.form["income1"]
        income2=request.form["income2"]
        expenses=request.form["expenses"]
        ssn=request.form["ssn"]
        workex=request.form["workex"]
        phone=request.form["phone"]
        name=request.form["name1"]
        data1=Loan(loan_amt, tenure, income1, income2, expenses, ssn, workex, name, phone)  
        final=int(data1.incometest())
        return redirect(url_for("templat", val=final))
    else:
        return render_template("index.html")

@app.route("/<val>")
def templat(val):
    if int(val)==1:
        return render_template('loan_accept.html')
    elif int(val)==2:
        return render_template('workex_reject.html')
    elif int(val)==3:
        return render_template('loan_rejected.html') 
    else:
        return render_template('fill_det.html')


if __name__ == "__main__":
    app.run(debug=True)

    
