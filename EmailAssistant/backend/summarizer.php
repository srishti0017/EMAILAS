<?php
// Simple script to handle spam detection (dummy logic)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $emailContent = file_get_contents('php://input');
    $spamWords = ['win', 'free', 'lottery'];
    $isSpam = false;

    foreach ($spamWords as $word) {
        if (stripos($emailContent, $word) !== false) {
            $isSpam = true;
            break;
        }
    }

    echo json_encode(['is_spam' => $isSpam]);
}
?>
