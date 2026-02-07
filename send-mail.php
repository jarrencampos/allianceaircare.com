<?php
// *********************
// CONTACT FORM SETTINGS
// *********************

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require 'phpmailer/Exception.php';
require 'phpmailer/PHPMailer.php';
require 'phpmailer/SMTP.php';

// Gmail SMTP settings
$gmailUser = 'jarren.campos.dev@gmail.com';
$gmailAppPassword = 'dwkl vdni cwvc xdjk'; // Replace with App Password from Google Account

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
$body .= "Message:\n$message\n\n Built by JC Tech Strategies";

// Send email using PHPMailer with Gmail SMTP
$mail = new PHPMailer(true);

try {
    // SMTP server settings
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->Username = $gmailUser;
    $mail->Password = $gmailAppPassword;
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587;

    // Recipients
    $mail->setFrom('jarren@goldmarkdigital.com', 'Alliance Air Care Website');
    $mail->addAddress('jarren@goldmarkdigital.com');
    $mail->addAddress('allianceaircare@gmail.com');
    $mail->addReplyTo($email, $name);

    // Content
    $mail->isHTML(false);
    $mail->Subject = '! New Form Submission !';
    $mail->Body = $body;

    $mail->send();
    echo "SUCCESS";
} catch (Exception $e) {
    echo "ERROR: Could not send email. {$mail->ErrorInfo}";
}
?>
