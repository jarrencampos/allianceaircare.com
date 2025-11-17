<?php
// *********************
// CONTACT FORM SETTINGS
// *********************
$to = "jarren@jctechstrategies.com";   // Your email address
$subject = "New Contact Form Submission";

// Get submitted form fields
$name    = htmlspecialchars(trim($_POST['name'] ?? ''));
$email   = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
$message = htmlspecialchars(trim($_POST['message'] ?? ''));

// Basic validation
if (!$name || !$email || !$message) {
    die("Please fill out all fields.");
}

// Build message body
$body  = "Name: $name\n";
$body .= "Email: $email\n\n";
$body .= "Message:\n$message\n";

// ********************************
// HostGator-safe email headers
// ********************************

// MUST be an email at your own domain
$fromAddress = "no-reply@jctechstrategies.com";

$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-type: text/plain; charset=utf-8\r\n";

// HostGator requires a domain-matching From:
$headers .= "From: Website Contact Form <{$fromAddress}>\r\n";

// You can still reply directly to the sender:
$headers .= "Reply-To: {$email}\r\n";

// Try sending the email
if (mail($to, $subject, $body, $headers)) {
    echo "SUCCESS";
} else {
    echo "ERROR: Could not send email.";
}
?>
