$(document).ready(function() {
    $(function(){
        $( "#datepicker" ).datepicker({
            dateFormat: 'dd-mm-yy',
            maxDate: '+3d',
            minDate: '-3d'
        });
    });

  });