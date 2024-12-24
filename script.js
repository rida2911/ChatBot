// Simulated OTP for demo purposes
let generatedOtp = Math.floor(1000 + Math.random() * 9000);
let otpVerified = false;

// Function to request OTP
function requestOtp() {
    const email = document.getElementById('email').value;
    if (email) {
        // Display simulated OTP (for demo)
        alert("Your OTP is: " + generatedOtp);
        document.getElementById('response').innerText = "OTP sent to your email!";
    } else {
        document.getElementById('response').innerText = "Please enter a valid email.";
    }
}

// Function to verify OTP and respond to the question
function verifyOtpAndAsk() {
    const otp = document.getElementById('otp').value;
    const question = document.getElementById('question').value.trim().toLowerCase();

    if (otp == generatedOtp) {
        otpVerified = true;
        if (question.includes("java")) {
            document.getElementById('response').innerText = "I will not give Java answers.";
        } else if (question) {
            // Provide a generic response for other programming questions
            document.getElementById('response').innerText = "That's a great question! Here’s some information on it: [provide resources or information here].";
        } else {
            document.getElementById('response').innerText = "Please enter a programming question.";
        }
    } else {
        otpVerified = false;
        document.getElementById('response').innerText = "Invalid OTP. Please try again.";
    }
}