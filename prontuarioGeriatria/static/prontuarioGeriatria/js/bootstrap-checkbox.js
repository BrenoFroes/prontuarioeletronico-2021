/**
 * bootstrap-checkbox.js
 * (c) 2013~ Jiung Kang
 * Licensed under the Apache License, Version 2.0 (the "License");
 */

(function($) {
  "use strict";

  console.log("oioi");
  var replaceCheckboxElement = function(checkbox, element) {
    var value = element.val(),
        id = element.attr('id'),
        className = element.attr('class'),
        style = element.attr('style'),
        checked = !!element[0].checked,
        welNew = $('<div></div>');

    element.replaceWith(welNew);

    if (id) { welNew.attr('id', id) }
    if (className) { welNew.attr('class', className) }
    welNew.addClass('bootstrap-checkbox');
    if (style) { welNew.attr('style', style); }
    if (checked) { welNew.addClass('checked'); }

    checkbox.value = value;
    checkbox.checked = checked;
    checkbox.element = welNew;
  };

  var changeCheckView = function(element, checked) {
    element.removeClass('ambiguous');
    element.removeClass('checked');

    if (checked === null) {
      element.addClass('ambiguous');
      element.html('<i class="icon-stop"></i>');
    } else if (checked) {
      element.addClass('checked');
      element.html('<i class="icon-ok"></i>');
    } else {
      element.html('');
    }
  };

  var attachEvent = function(checkbox, element) {
    element.on('click', function(e) {
      var checked;
      if (checkbox.checked) {
        checked = false;
      } else if (checkbox.checked === false && checkbox.ambiguous === true){
        checked = null;
      } else {
        checked = true;
      }

      checkbox.checked = checked;
      changeCheckView(checkbox.element, checked);

      checkbox.element.trigger({
        type: 'check',
        value: checkbox.value,
        checked: checked,
        element: checkbox.element
      });
    });
  };

  var Checkbox = function(element, options) {
    replaceCheckboxElement(this, element);
    attachEvent(this, this.element);
    if (options && options.label) {
      attachEvent(this, $(options.label));
    }
  };

})