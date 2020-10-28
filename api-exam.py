from flask import Flask
from flask_restful import Api, Resource
from datetime import date
from datetime import datetime
import requests

app = Flask(__name__)
api = Api(app)

class PremiumPayment():
	amount = None
	crdCardNum = None 
	cardHold = None

	def post():
		#post a request for payment
		#result = post # True | False 
		#return true | false
		return true

class ExpensivePayment():
	amount = None
	crdCardNum = None 
	cardHold = None

	def post():
		#post a request for payment
		#result = post # True | False 
		#return true | false
		return true

	def available():
		#request if available
		#result = based on request
		#return true | false
		return true

class CheapPayment():
	amount = None
	crdCardNum = None 
	cardHold = None

	def post():
		#post a request for payment
		#result = post # True | False 
		#return true | false
		return true

#Class with Security Code as paramater
class Payment(Resource): 

	def post(self, crdCardNum, cardHold, expDate, secCode, amount):
		try:
			selected_date = datetime.strptime(expDate,"%m-%d-%Y").date()

			if selected_date < date.today():
				return {"status": 400}

			amt = decimal(amount)

			if (amt <= 20.0):
				p = CheapPayment()
				p.amount = amount
				p.cardHold = cardHold
				p.crdCardNum = crdCardNum
				result = p.post()
				if result:
					return {"status": 200}
				else:
					return {"status": 400}
			elif (amt > 20.0 and amt <= 500.0):
				p = ExpensivePayment()
				if not p.available():
					p = CheapPayment()
				p.amount = amount
				p.cardHold = cardHold
				p.crdCardNum = crdCardNum
				result = p.post()
				if result:
					return {"status": 200}
				else:
					return {"status": 400}
			else:
				p = PremiumPayment()
				p.amount = amount
				p.cardHold = cardHold
				p.crdCardNum = crdCardNum
				for x in range(3):
					result = p.post()
					if not result:
						continue
					else:
						break
				if result:
					return {"status": 200}
				else:
					return {"status": 400}

			return {"status": 200 }

		except:
			return {"status": 500 }  

#Class without Security Code as paramater
class Payment1(Resource):

    def post(self, crdCardNum, cardHold, expDate, amount):
        try:
            selected_date = datetime.strptime(expDate, "%m-%d-%Y").date()
            
            if selected_date < date.today():
                return {"status": 400}

            amt = decimal(amount)

            if (amt <= 20.0):
                p = CheapPayment()
                p.amount = amount
                p.cardHold = cardHold
                p.crdCardNum = crdCardNum
                result = p.post()
                if result:
                    return {"status": 200}
                else:
                    return {"status": 400}
            elif (amt > 20.0 and amt <= 500.0):
                p = ExpensivePayment()
                if not p.available():
                    p = CheapPayment()

                p.amount = amount
                p.cardHold = cardHold
                p.crdCardNum = crdCardNum
                result = p.post()
                if result:
                    return {"status": 200}
                else:
                    return {"status": 400}
            else:
                p = PremiumPayment()
                p.amount = amount
                p.cardHold = cardHold
                p.crdCardNum = crdCardNum
				for x in range(3):
					result = p.post()
					if not result:
						continue
					else:
						break
				if	result:
					return {"status": 200}
				else:
					return {"status": 400}

            return {"status": 200 }

        except:
          return {"status": 500 } 

api.add_resource(Payment, "/Payment/<string:crdCardNum>/<string:cardHold>/<string:expDate>/<string:secCode>/<string:amount>")
api.add_resource(Payment1, "/Payment/<string:crdCardNum>/<string:cardHold>/<string:expDate>/<string:amount>")

if __name__ == "__main__":
    app.run(debug=True)