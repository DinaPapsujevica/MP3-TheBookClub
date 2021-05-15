$(document).ready(function() {
    $(function(){
        $( "#datepicker" ).datepicker({
            dateFormat: 'dd-mm-yy',
            maxDate: '+3d',
            minDate: '-3d'
        });
    });
    const fileSelector = document.getElementById('image_url');
    fileSelector.addEventListener('change', (event) => {
        const fileList = event.target.files;
        console.log(fileList);
    });
  });