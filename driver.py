import os
import sys
import pickle
from temp_detect import TempDetect
from send_sms import SendSMS
from send_mail import SendEmail

class Driver():
	def __init__(self):
		dictfile = open('contacts_info.txt', 'rb')
		self.contacts_dict = pickle.load(dictfile)
		dictfile.close()
		self.smsobj = SendSMS()
		self.mailobj = SendEmail()

	def get_image(self):
		latest_file = '/home/pi/Pictures/server/image.jpg'
		return latest_file

	def detect_digit(self):
		subject = 'Temperature Alert'
		negmsg = 'Unable to detect successfully. Detects: '
		alertmsg = 'Temperature beyond acceptable range. The display reads : '
		img_path = self.get_image()
		tobj = TempDetect(img_path=img_path)
		digits = []

		try:
			# First attempt to detect. cv2.dilate() value = 1
			digits = tobj.final_call(iterval=1)
			#digits2 = digits[:2]
			digits_str = ''.join(str(x) for x in digits)
			# Unable to map to a digit (returns -1) or detects no digit
			if -1 in digits or len(digits)<1:
				# Second attempt to detect. cv2.dilate() value = 2
				digits = tobj.final_call(iterval=2)
				digits_str = ''.join(str(x) for x in digits)
				# Unable to detect second time
				if -1 in digits or len(digits)<1:
					message = negmsg+(digits_str[:3])
					for key in self.contacts_dict:
						if self.contacts_dict[key]['status'] != 'Inactive':
							self.mailobj.sendMail(self.contacts_dict[key]['mailid'], subject, message, img_path)
							if self.contacts_dict[key]['mnum'] != '':
								self.smsobj.sendSMS(message, self.contacts_dict[key]['mnum'])
					sys.exit()

				#Else, successfully detected (2nd attempt)
			#Else, successfully detected (1st attempt)
			message = alertmsg+(digits_str[:3])
			for key in self.contacts_dict:
				if self.contacts_dict[key]['status'] != 'Inactive':
					if not self.contacts_dict[key]['mint'] < digits_str < self.contacts_dict[key]['maxt']:
						self.mailobj.sendMail(self.contacts_dict[key]['mailid'], subject, message, img_path)
						if self.contacts_dict[key]['mnum'] != '':
							self.smsobj.sendSMS(message, self.contacts_dict[key]['mnum'])

					else:
						# Within the given range. Do nothing.
						pass

		except Exception as exception:
			msg = 'ERROR: ' + type(exception).__name__
			self.mailobj.sendMail(self.contacts_dict['Shwetha']['mailid'], subject, msg, img_path)
			sys.exit()



mainobj = Driver()
mainobj.detect_digit()