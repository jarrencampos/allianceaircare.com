<?php
// *********************
// CONTACT FORM SETTINGS
// *********************
$to = "jarren@jctechstrategies.com";   // Destination email
$subject = "New Contact Form Submission";

// Get submitted form fields (sanitized)
$name     = htmlspecialchars(trim($_POST['name'] ?? ''));
$email    = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
$phone    = htmlspecialchars(trim($_POST['phone'] ?? ''));
$zipcode  = htmlspecialchars(trim($_POST['zipcode'] ?? ''));
$service  = htmlspecialchars(trim($_POST['service'] ?? ''));
$message  = htmlspecialchars(trim($_POST['message'] ?? ''));

// Basic validation
if (!$name || !$email || !$phone || !$zipcode || !$service || !$message) {
    die("Please fill out all required fields.");
}

// Build email message body
$body  = "New Contact Form Submission\n\n";
$body .= "Name: $name\n";
$body .= "Email: $email\n";
$body .= "Phone: $phone\n";
$body .= "Zip Code: $zipcode\n";
$body .= "Service Requested: $service\n\n";
$body .= "Message:\n$message\n";

// ********************************
// HostGator-safe email headers
// ********************************

// MUST be an email at your domain
$fromAddress = "no-reply@allianceaircare.com";

$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-type: text/plain; charset=utf-8\r\n";

// Required by HostGator
$headers .= "From: Website Contact Form <{$fromAddress}>\r\n";

// Allows direct email reply to sender
$headers .= "Reply-To: {$email}\r\n";

// Try sending the email
if (mail($to, $subject, $body, $headers)) {
    echo "SUCCESS";
} else {
    echo "ERROR: Could not send email.";
}
?>
