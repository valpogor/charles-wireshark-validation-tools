    $("#input-file").on("change",function(){
        var reg=/(.jpg|.gif|.png)$/;
        if (!reg.test($("#input-file").val())) {
            alert('Invalid File Type');
            return false;
        }
        uploadFile();
    });
    $("#choose-photo").on("click",function(){
        $('#input-file').click();
    });
    function uploadFile()
    {
        $("#upload").ajaxSubmit({
            dataType: 'json',
            success: function(data, statusText, xhr, wrapper){
                $('#display-image').prop("src","/assets/images/tmp/"+data);
                //update relevent product form fields here
            }
        });
    }

