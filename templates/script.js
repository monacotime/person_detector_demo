$("#live_btn").click(function(){
    //go live btn
    console.log("live clicked")

    //clean element
    $("#feed_container").empty()
    $("#feed_container").append('<img id = "feed" src="http://localhost:5000/video_feed">')
});

console.log($(".control_checkbox"))

function get_config(){
    var config = {}
    $('.control_checkbox').each(function(){
        let id = $(this).attr('id')
        let state = "False"
        if ($('#segmentation_mask').attr('checked') !== undefined){
            state = "True"
        }
        config[id] = state
    })
    return config
}

console.log(JSON.stringify(get_config()))
$("#config_display").empty()
$('#config_display').html("<span>"+get_config()+"</span>")