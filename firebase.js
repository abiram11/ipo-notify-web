// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCUjQJuFbe5hAkpErYztDwLX0-l0MWAovY",
  authDomain: "ipo-notify-4d4c9.firebaseapp.com",
  projectId: "ipo-notify-4d4c9",
  storageBucket: "ipo-notify-4d4c9.appspot.com",
  messagingSenderId: "118866062782",
  appId: "1:118866062782:web:6e421c6c88b9fe126f1def",
  measurementId: "G-ZX6D76QYS9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);