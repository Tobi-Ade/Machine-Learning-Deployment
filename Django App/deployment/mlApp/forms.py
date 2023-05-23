from django import forms

class form_inputs(forms.Form):
    product_options = [
        ('Mortgage', 'Mortgage'), ('Debt Collection', 'Debt'), ('Credit reporting', 'Credit'),
        ('Credit card', 'Credit card'), ('Bank account', 'Bank account'), ('Consumer Loan', 'Consumer Loan'),
        ('Student loan', 'Student loan'), ('Payday loan', 'Payday loan'), ('Money transfers', 'Money transfers'),
        ('Prepaid card', 'Prepaid card'), ('Virtual currency', 'Virtual currency')
    ]
    product_type = forms.ChoiceField(choices=product_options, widget=forms.Select(attrs={"width": 780}))

    issue_options = [
        ('Loan modification,collection,foreclosure', 'Loan modification, collection, foreclosure'),
        ('Incorrect information on credit report', 'Incorrect information on credit report'),
        ('Loan servicing, payments, escrow account', 'Loan servicing, payments, escrow account'),
        ("Cont'd attempts collect debt not owed", "Cont'd attempts collect debt not owed"),
        ("Account opening, closing, or management", "Account opening, closing, or management"),
        ("Disclosure verification of debt", "Disclosure verification of debt"),
        ("Deposits and withdrawals", "Deposits and withdrawals"),
        ("Communication tactics", "Communication tactics"),
        ("Application, originator, mortgage broker", "Application, originator, mortgage broker"),
        ("Billing disputes", "Billing disputes")
    ]

    issue_type = forms.ChoiceField(choices=issue_options)

    consent_options = [
        ('Consent provided', 'Consent provided'), ('Consent not provided', 'Consent not provided'),
        ('Consent withdrawn', 'Consent withdrawn')
        ]
    consent_type = forms.ChoiceField(choices=consent_options)

    submission_options = [
        ('Web', 'Web'), ('Fax', 'Fax'), ('Referral', 'Referral'), ('Postal Mail', 'Postal Mail'),
        ('Phone', 'Phone'), ('Email', 'Email')
    ]
    submitted_via = forms.ChoiceField(choices=submission_options)

    company_response_options = [
        ('Closed with explanation', 'Closed with explanation'), ('Closed', 'Closed'),
        ('Closed without relief', 'Closed without relief'), ('In progress', 'In progress'),
        ('Closed with non-monetary relief', 'Closed with non-monetary relief'),
        ('Closed with relief', 'Closed with relief'), ('Untimely response', 'Untimely response')
    ]
    company_response = forms.ChoiceField(choices=company_response_options)

    timely_response_options = [
        ('1', 'Yes'), ('0', 'No')
    ]
    timely_response = forms.ChoiceField(choices=timely_response_options)

    years = [
        ('2011','2011' ), ('2012','2012' ), ('2013','2013' ), ('2014','2014'),
        ('2015','2015' ), ('2016','2016' ), ('2017','2017')
    ]
    year = forms.ChoiceField(choices=years)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['product_type'].widget.attrs.update({'class': 'options'})








