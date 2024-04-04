import "./App.css";
import Chatbot from "./components/ChatBot";
import Header from "./components/Header";
import { useState } from 'react'

function App() {

  const [selectedFile, setSelectedFile] = useState({
    file: null,
    document_id: null,
  });


  const handleFileChange = (event) => {
    setSelectedFile(
      {
        file: event.target.files[0],
        document_id: null,
      });
  };

  console.log(selectedFile);

  const handleSubmit = async () => {
    if (!selectedFile) {
      alert('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile.file);

    console.log('Uploading file...');
    try {
      const response = await fetch('http://localhost:8000/upload/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Upload failed');
      }

      response.json().then((data) => {setSelectedFile(prev => ({...prev, document_id: data.document_id}))});

      alert('File uploaded successfully!');
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Error uploading file. Please try again.');
    }
  };

  return (
    <>
    <Header handleSubmit={handleSubmit} handleFileChange={handleFileChange} />
    <Chatbot selectedFile={selectedFile} />
    </>
  );
}

export default App;
