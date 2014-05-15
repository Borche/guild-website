from django.forms import ModelForm, ChoiceField
from django.forms.fields import IntegerField
from captcha.fields import CaptchaField

from recruitment.models import Application

class ApplicationForm(ModelForm):
	classes = [
		('Mage','Mage'),
		('Warrior','Warrior'),
		('Druid','Druid'),
		('Rogue','Rogue'),
		('Warlock','Warlock'),
		('Hunter','Hunter'),
		('Death Knight','Death Knight'),
		('Monk','Monk'),
		('Paladin','Paladin'),
		('Shaman','Shaman'),
		('Priest','Priest'),
	]
	sorted_classes = sorted(classes, key=lambda tup: tup[0])
	h = 'Human'
	ne = 'Night Elf'
	d = 'Draenei'
	dw = 'Dwarf'
	w = 'Worgen'
	g = 'Gnome'
	p = 'Pandaren'
	races = [
		(h,h),
		(ne,ne),
		(d,d),
		(dw,dw),
		(w,w),
		(g,g),
		(p,p),
	]
	sorted_races = sorted(races, key=lambda tup: tup[0])
	xclass = ChoiceField(choices=sorted_classes, label='Class')
	race = ChoiceField(choices=sorted_races)
	level = IntegerField(min_value=1, max_value=100)
	item_level = IntegerField(min_value=1, max_value=800)
	age = IntegerField(min_value=18, max_value=100)
	captcha = CaptchaField()
	class Meta:
		model = Application
		fields = ['email', 'name', 'age', 'character_name', 'race', 'xclass', 
			'level', 'item_level', 'message']
		exclude = ['header', 'date']      

