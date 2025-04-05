# this is the streamlit web app version of the notebook
# this code will generate a clean ui to demonstrate the project
from pdfminer.high_level import extract_text
import streamlit as st
import pickle
import re

def clean_data(text):
    # remove hyperlinks
    text = re.sub(r'http\S+\s', ' ', text)
    # remove special sequence
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'RT|cc', ' ', text)
    text = re.sub(r'[^\x00-\x7f]', ' ', text)
    # remove mentions and hashtags
    text = re.sub(r'@\S+\s', ' ', text)
    text = re.sub(r'#\S+\s', ' ', text)
    # remove . and - if they are not between words
    text = re.sub(r'(?<!\w)[^\w\s.-]+|[^\w\s.-]+(?!\w)', '', text)
    # remove full stops
    text = re.sub(r'(?<=\w)\.(?!\w)', '', text)
    # remove hyphens
    text = re.sub(r'(?<=\w)-(?!\w)|(?<!\w)-|-(?!\w)', '', text)
    # lower text
    text = text.lower()

    return text

index2target = {0: 'Advocate', 1: 'Arts', 2: 'Automation Testing',
 3: 'Blockchain', 4: 'Business Analyst', 5: 'Civil Engineer',
 6: 'Data Science', 7: 'Database', 8: 'DevOps Engineer', 9: 'DotNet Developer',
 10: 'ETL Developer', 11: 'Electrical Engineering', 12: 'HR', 13: 'Hadoop',
 14: 'Health and fitness', 15: 'Java Developer', 16: 'Mechanical Engineer',
 17: 'Network Security Engineer', 18: 'Operations Manager', 19: 'PMO',
 20: 'Python Developer', 21: 'SAP Developer', 22: 'Sales', 23: 'Testing', 24: 'Web Designing'}

# import pretrained model
clf = pickle.load(open('./data/model.pkl', 'rb'))

# import pretrained vectorizer
vectorizer = pickle.load(open('./data/vectorizer.pkl', 'rb'))

# web app
def main():
    
    st.title('Resume Screening App 📝')

    # upload resume ui
    uploaded_file = st.file_uploader(type = ['pdf'], label = 'Upload your resume to see the predicted category')

    if uploaded_file :
        resume_text = extract_text(uploaded_file)

        # clean resume
        cleaned_resume = clean_data(resume_text)
        
        # input features 
        input_features = vectorizer.transform([cleaned_resume])

        # predict and id
        pred = clf.predict(input_features)[0]

        # find category
        predicted_category = index2target.get(pred, 'Unknown')

        st.write('Predicted Category :', predicted_category)

if __name__ == '__main__':
    main()