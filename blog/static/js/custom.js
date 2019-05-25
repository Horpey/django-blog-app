function bookmark(postid,postTitle) {
    toastrMsg = postTitle;
    toastr.info('Bookmarked !!!',toastrMsg,options = {
        tapToDismiss: true,
        iconClass: 'toast-info',
        positionClass: 'toast-bottom-right',
        timeOut: 5000, // Set timeOut to 0 to make it sticky
        titleClass: 'toast-title',
        messageClass: 'toast-message'
      } );
    
}