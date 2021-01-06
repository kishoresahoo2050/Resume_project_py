from django import forms

class ContactFrm(forms.Form):
    name = forms.CharField(label="Your Name",label_suffix=" ",error_messages={"required":"Your Name Must Be Required"},widget=forms.TextInput(attrs={
        "class":"form-control",
        "id"   :"name",
        "placeholder":"Enter Your Name "
    }))
    email = forms.EmailField(label="Your Email",label_suffix=" ",error_messages={"required":"Your Email Must Be Required"},widget=forms.TextInput(attrs={
        "class":"form-control",
        "id"   :"email",
        "placeholder":"Enter Your Email "
    }))
    subject = forms.CharField(label="Your Subject",label_suffix=" ",error_messages={"required":"Your Subject Must Be Required"},widget=forms.Textarea(attrs={
        "class":"form-control",
        "id"   :"sub",
        "placeholder":"Enter Your Subject ",
        "cols":"",
        "rows":""
    }))
    msg = forms.CharField(label="Your Message",label_suffix=" ",error_messages={"required":"Your Message Must Be Required"},widget=forms.Textarea(attrs={
        "class":"form-control",
        "id"   :"msg",
        "placeholder":"Enter Your Message ",
        "cols":"",
        "rows":""
    }))