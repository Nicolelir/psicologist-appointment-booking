$(document).ready(function() {
    $('#contact-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission
        
        var formData = $(this).serialize(); // Serialize form data
        
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'), // Form action URL
            data: formData,
            success: function(response) {
                // Handle success response here (e.g., show success message)
                console.log('Form submitted successfully');
            },
            error: function(xhr, status, error) {
                // Handle error response here (e.g., show error message)
                console.error('Form submission error:', error);
            }
        });
    });
});