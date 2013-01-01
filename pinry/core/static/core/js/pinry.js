/**
 * Based on Wookmark's endless scroll.
 */
var apiURL = '/api/pin/?format=json&offset='
var page = 0;
var handler = null;
var globalTag = null;
var isLoading = false;

/**
 * When scrolled all the way to the bottom, add more tiles.
 */
function onScroll(event) {
  if(!isLoading) {
      var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
      if(closeToBottom) loadData();
  }
};

function applyLayout() {
  $('#pins').imagesLoaded(function() {
      // Clear our previous layout handler.
      if(handler) handler.wookmarkClear();
      
      // Create a new layout handler.
      handler = $('#pins .pin');
      handler.wookmark({
          autoResize: true,
          offset: 10,
          itemWidth: 280,
          container: $('#pins')
      });
  });
};

/**
 * Loads data from the API.
 */
function loadData(tag) {
    isLoading = true;
    $('#loader').show();

    if (tag !== undefined) {
        globalTag = tag;
        window.history.pushState(tag, 'Pinry - Tag - '+tag, '/pins/tag/'+tag+'/');
    } else if (url(2) == 'tag') { //hard coded way to detect user input tag url
        tag = url(3);
        globalTag = tag;
        window.history.pushState(tag, 'Pinry - Tag - '+tag, '/pins/tag/'+tag+'/');
    }

    if (tag !== undefined) {
        $('#pins').html('');
        page = 0;
        if (tag != null)
            $('.tags').html('<span class="label tag" onclick="loadData(null)">' + tag + ' x</span>');
        else {
            $('.tags').html('');
            window.history.pushState(tag, 'Pinry - Recent Pins', '/pins/');
        }
    }

    var loadURL = apiURL+(page*30);
    if (globalTag !== null) loadURL += "&tag=" + tag;
    
    $.ajax({
        url: loadURL,
        success: onLoadData
    });
};

/**
 * Receives data from the API, creates HTML for images and updates the layout
 */
function onLoadData(data) {
    data = data.objects;
    isLoading = false;
    $('#loader').hide();
    
    page++;
    
    var html = '';
    var i=0, length=data.length, image;
    for(; i<length; i++) {
      image = data[i];
    //  if(image.valid)
      {
      html += '<div class="pin">';
          html += '<div class="pin-options">';
              html += '<a href="/pins/delete-pin/'+image.id+'">';
                  html += '<i class="icon-trash"></i>';
              html += '</a>';
          html += '</div>';
          html += '<a class="fancybox" rel="pins" href="'+image.image+'">';
              html += '<img src="'+image.thumbnail+'" width="200" >';
          html += '</a>';
          if (image.description) html += '<p>'+image.description+'</p>';
          if (image.tags) {
              html += '<p>';
              for (tag in image.tags) {
                  html += '<span class="label tag" onclick="loadData(\'' + image.tags[tag] + '\')">' + image.tags[tag] + '</span> ';
              }
              html += '</p>';
          }
          html += "<div class='write convo clearfix' style='display:block'><a href='//' title='' class='img x'><img style='width:30px; height:30px'  src='/static/core/img/error.png'></a><form action='/pins/39085496/comments/' method='POST'> <textarea style='background-color: rgb(255, 255, 255);' autocomplete='off' placeholder='添加评论或把采集@给好友' class='GridComment ani-affected '></textarea><ul style='display: none; z-index: 42; opacity: 0;' class='ac-choices'></ul><a href='#' onclick='return false;' class='grid_comment_button'></a></form></div>";
      html += '</div>';
      }
    }
    
    $('#pins').append(html);
    
    applyLayout();
};

$(document).ready(new function() {
    $(document).bind('scroll', onScroll);
    loadData();
});

/**
 * On clicking an image show fancybox original.
 */
$('.fancybox').fancybox({
    openEffect: 'none',
    closeEffect: 'none'
});
