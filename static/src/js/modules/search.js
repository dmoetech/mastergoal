


module.exports = function () {
  	$('.search-toggle').on('click', e => {
    	$('.search-box, .search-input').toggleClass('active');
    	$('.search-input input').focus();
    	e.preventDefault();
  	});
}();