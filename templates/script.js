// image selector -----------------------------------------//

$(".sel_imgs").click(function(){
    // console.log($(this).get())
    // console.log($(this).prop('src'))
    $("#im_feed").attr('src', $(this).prop('src'))
})










// Config display -----------------------------------------//

// function get_config(){
//     var config = {}
//     $('.control_checkbox').each(function(){
//         let id = $(this).attr('id')
//         let state = "False"
//         if ($('#segmentation_mask').attr('checked') !== undefined){
//             state = "True"
//         }
//         config[id] = state
//     })
//     return config
// }

// console.log($(".control_checkbox"))
// console.log(JSON.stringify(get_config()))
// $("#config_display").empty()
// $('#config_display').html("<span>"+get_config()+"</span>")

// Live Feed -------------------------------------------------//
$("#live_btn").click(function(){
    //go live btn
    console.log("live clicked")

    //clean element
    $("#im_feed").attr('src', '')
    $("#feed_container").empty()

    //append feed
    $("#feed_container").append('<img id = "feed" src="http://localhost:5000/video_feed">')
});