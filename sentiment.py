def sentim(polarity):
	if polarity==2:
		sentiment='Neutral'
	elif polarity==0:
		sentiment='Negative'
	elif polarity==4:
		sentiment='Positive'
	else:
		sentiment='Could not be determined!'
	return sentiment