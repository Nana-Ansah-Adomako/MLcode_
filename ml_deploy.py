import pickle
import pandas as pd
import streamlit as st
import time
import smtplib
from email.message import EmailMessage


# Function to send email
def send_email(to_email, loan_status):
    msg = EmailMessage()
    msg.set_content(f"Your loan application status: {loan_status}")

    msg['Subject'] = 'Loan Application Status'
    msg['From'] = 'nanaadomakoansah@gmail.com'  # Update with your email
    msg['To'] = to_email

    # Send email via Gmail SMTP server
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('nanaadomakoansah@gmail.com', 'bgllgzpffyqoqlzv')  # Use App Password
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPRecipientsRefused as e:
        st.error(f"Error: Unable to send email to {to_email}. Please check the recipient address.")


# Load the trained model
loaded_model = pickle.load(open("DT_model.sav", "rb"))

# Function for loan prediction
Loan_decline_message = "\nDear Applicant,\n" \
                       "\nWe are writing to inform you about your recent loan application status with our institution." \
                       " After careful review, we regret that your application has been declined.\n" \
                       "\nThe decision was based on various factors. Our policies require us to ensure our clients' financial stability for both their protection and ours." \
                       "Unfortunately, at this time, we believe that granting the requested loan may cause financial strain.\n" \
                       "\nWe appreciate your trust in our institution and apologize for any inconvenience this may cause." \
                       "We invite you to reapply after a period to allow for any changes in your financial circumstances to take effect." \
                       "We remain at your disposal should you need any further assistance or clarification regarding this matter.\n" \
                       "\nBest Regards," \
                       "\nCredit and Risk Assessment Team," \
                       "\nALAS Banking Services."



Loan_acceptance_message = "\nDear Applicant,\n" \
                          "\nWe are pleased to inform you that your loan application has been considered. " \
                          "We understand the importance of this loan and the role it plays in helping you reach your financial goals.\n" \
                          "\nwe will begin processing the transfer immediately. " \
                          "We want to make sure that you have everything you need, so please don’t hesitate to contact us if there are any additional questions or concerns.\n" \
                          "\nThank you for choosing us for your financial needs. We wish you all the best as you take this next step in growing your business!\n" \
                          "\nBest Regards," \
                          "\nCredit and Risk Assessment Team," \
                          "\nALAS Banking Services."


def loan_prediction(input_data):
    input_data_df = pd.DataFrame([input_data], columns=[
        'Gender', 'Education', 'Marital_Status', 'Employment_Type', 'Residential_Status', 'Dependents',
        'Applicant_Monthly_Income', 'Loan_Amount', 'Loan_Type', 'Term_of_Loan'
    ])
    # Type casting for data consistency
    input_data_df = input_data_df.astype({
        'Gender': 'object', 'Education': 'object', 'Marital_Status': 'object', 'Employment_Type': 'object',
        'Residential_Status': 'object', 'Dependents': 'object', 'Applicant_Monthly_Income': 'object',
        'Loan_Amount': 'int64', 'Loan_Type': 'object', 'Term_of_Loan': 'int64',
    })
    prediction = loaded_model.predict(input_data_df)
    return Loan_acceptance_message if prediction[0] == 'Y' else Loan_decline_message


# Main app

def add_image_top_right(image_path):
    st.markdown(
        f"""
        <style>
        .image-container {{
            position: absolute;
            top: 5px;
            right: 1px;
        }}
        </style>
        <div class="image-container">
            <img src="data:image/jpeg;base64,{img_to_base64(image_path)}" width="100">
        </div>
        """, unsafe_allow_html=True
    )

    # Function to convert image to base64
def img_to_base64(image_path):
    import base64
    with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()

# CSS to change the style of st.title
def apply_custom_css():
    st.markdown(
        """
        <style>
        h1 {
            font-family: 'Arial', sans-serif;
            color: #FFFFFF;
            font-size: 35px;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True
    )

def main():
    apply_custom_css()
    st.title("AUTOMATED LOAN APPLICATION SYSTEM")
    add_image_top_right("D:\\microloan.png")

    # Navigation with the "Applicant Details" first and "Loan Application" second
    page = st.sidebar.selectbox("Choose a page", ["Applicant Details", "Loan Application"])

    if page == "Applicant Details":
        st.subheader("Enter your details")
        name = st.text_input("Name")
        email = st.text_input("Email")
        contact = st.text_input("Contact Number")
        address = st.text_input("Digital Address")
        ID = st.text_input("Ghana Card ID No:")

        if st.button("Submit Details"):
            st.write(f"Thank you, {name}. Please proceed to fill out the loan application form.")
            st.session_state['Applicant_details'] = {'name': name, 'email': email}

    elif page == "Loan Application":
        if 'Applicant_details' not in st.session_state:
            st.error("Please submit your  details before applying for the loan.")
            return

        # Loan Application Inputs
        st.subheader("Loan Application Form")
        Gender = st.selectbox(label="Gender", options=["Male", "Female"])
        Education = st.selectbox(
            label="Education Background", options=["Graduate", "Not Graduate"])
        Marital_Status = st.selectbox(label="Marital Status", options=["Married", "Divorced", "Widowed", "Single"])
        Employment_Type = st.selectbox(label="Employment Type", options=["Government", "Private", "Self Employed"])
        Residential_Status = st.selectbox(label="Residential Status",
                                          options=["Own", "Living with Parents", "Employer Provided", "Rent"])
        Dependents = st.selectbox(label="Number of Dependents", options=["0", "1", "2", "3+"])
        Applicant_Monthly_Income = st.selectbox(label="Applicant's Monthly Income",
                                                options=["1500-2000", "2000-3500", "4500-6000", "6000-8000",
                                                         "8000-10000", "10000-15000", "15000-20000", " >20000"])
        Loan_Amount = st.text_input("Loan Amount")
        Loan_Type = st.selectbox(label="Type of Loan", options=["FTL", "RTL"])
        Term_of_Loan = st.selectbox(label="Loan Term (in months)", options=["6", "12", "24", "36"])

        if st.button("Submit Application"):
            # Call loan prediction function
            loan_status = loan_prediction([Gender, Education, Marital_Status, Employment_Type, Residential_Status,
                                           Dependents, Applicant_Monthly_Income, Loan_Amount, Loan_Type, Term_of_Loan])

            st.session_state['loan_status'] = loan_status
            st.success("Loan Application Submitted!")

            # Send the email
            email = st.session_state['Applicant_details']['email']
            with st.spinner("Processing... You will receive the response in an hour."):
                time.sleep(5)  # Simulating the delay (replace with time.sleep(3600) for 1 hour)
            send_email(email, st.session_state['loan_status'])
            st.success(f"Loan status has been sent to {email}!")


if __name__ == '__main__':
    main()
