(function($) {
  $.fn.removeClasses = function(classes) {
    return this.removeClass(classes.join(' '));
  };
  $.fn.switchify = function(config) {
    config = config || {};
    var prefix   =           config.prefix   || 'range-';
    var onCls    = prefix + (config.onCls    || 'on'   );
    var offCls   = prefix + (config.offCls   || 'off'  );
    var unsetCls = prefix + (config.unsetCls || 'unset');
    var $self = this;
    return this.on('change', function(e) {
      var value = parseInt(this.value, 10);
      switch (value) {
        case 1  :  return $self.removeClasses([unsetCls, offCls]).addClass(onCls);
        case 2  :  return $self.removeClasses([onCls, offCls]).addClass(unsetCls);
        case 3  :  return $self.removeClasses([onCls, unsetCls]).addClass(offCls);
        default :  return $self;
      }
    });
  };
})(jQuery);

$('#range-filter').switchify({
   onCls    : 'active',
   offCls   : 'passive',
   unsetCls : 'all'
}).on('change', function(e) {
  var $self = $(this);
  if      ($self.hasClass('range-active'))  $('span').text('Active');
  else if ($self.hasClass('range-passive')) $('span').text('Passive');
  else if ($self.hasClass('range-all'))     $('span').text('All');
  else                                      $('span').text('Error!');
});