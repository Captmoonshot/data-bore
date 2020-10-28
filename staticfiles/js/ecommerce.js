

$(document).ready(function(){

          // AutoSearch
          var searchForm = $(".search-form")
          var searchInput = searchForm.find("[name='q']") // input name='q'
          var typingTimer;
          var typingInterval = 1000 // 1 second
          var searchBtn = searchForm.find("[type='submit']")

          searchInput.keyup(function(event){
            // key released
            clearTimeout(typingTimer)
            typingTimer = setTimeout(performSearch, typingInterval)
          })

          searchInput.keydown(function(event){
            // key pressed
            clearTimeout(typingTimer)
          })

          function displaySearching(){
            searchBtn.addClass("disabled")
            searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...")
          }

          function performSearch(){
            displaySearching()
            var query = searchInput.val()
            setTimeout(function(){
              window.location.href = '/search/?q=' + query
            }, 1400)
          }


          // Cart + Add Products
          var productForm = $(".form-product-ajax") // #form-product-ajax

          function getOwnedProduct(productId, submitSpan){
            var actionEndpoint = '/orders/endpoint/verify/ownership/'
            var httpMethod = 'GET'
            var data = {
              product_id: productId
            }

            var isOwner;
            $.ajax({
              url: actionEndpoint,
              method: httpMethod,
              data: data,
              success: function(data){
                console.log(data)
                console.log(data.owner)
                if (data.owner){
                  isOwner = true
                  submitSpan.html("<div class='btn-block'><a class='p-3 mb-2 bg-dark text-white' href='/library/'>In Library <i class='fa fa-book' aria-hidden='true'></i></a>&nbsp;&nbsp;&nbsp;</div></br>")
                } else {
                  isOwner = false
                }
              },
              error: function(error){
                console.log(error)
              }

            })
            return isOwner

        }

          $.each(productForm, function(index, object){
            var $this = $(this)
            var isUser = $this.attr("data-user")
            var submitSpan = $this.find(".submit-span")
            var productInput = $this.find("[name='product_id']")
            var productId = productInput.attr("value")
            var productIsDigital = productInput.attr("data-is-digital")

            if (productIsDigital && isUser){
              var isOwned = getOwnedProduct(productId, submitSpan)
            }
            
          })

          productForm.submit(function(event){
              event.preventDefault();
              // console.log("Form is not sending")
              var thisForm = $(this)
              // var actionEndpoint = thisForm.attr("action"); // API Endpoint
              var actionEndpoint = thisForm.attr("data-endpoint")
              var httpMethod = thisForm.attr("method");
              var formData = thisForm.serialize();

              $.ajax({
                url: actionEndpoint,
                method: httpMethod,
                data: formData,
                success: function(data){
                  var submitSpan = thisForm.find(".submit-span")
                  if (data.added){
                    submitSpan.html("<div class='btn-block'><a class='p-3 mb-2 bg-dark text-white' href='/cart/'>In Cart <i class='fa fa-shopping-cart' aria-hidden='true'></i></a></br>")
                  } else {
                    // submitSpan.html("<button type='submit'  class='btn btn-success'>Add to cart</button>")
                   }
                  var navbarCount = $(".navbar-cart-count")
                  navbarCount.text(data.cartItemCount)
                  var currentPath = window.location.href

                  if (currentPath.indexOf("cart") != -1) {
                    refreshCart()
                  }
                },
                error: function(errorData){
                  console.log("error")
                  console.log(errorData)
                }
              })

          })

          function refreshCart(){
            console.log("in current cart")
            var cartTable = $(".cart-table")
            var cartBody = cartTable.find(".cart-body")
            //cartBody.html("<h1>Changed</h1>")
            var productRows = cartBody.find(".cart-product")
            var currentUrl = window.location.href

            var refreshCartUrl = '/api/cart/'
            var refreshCartMethod = "GET";
            var data = {};
            $.ajax({
              url: refreshCartUrl,
              method: refreshCartMethod,
              data: data,
              success: function(data){
                
                var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
                if (data.products.length > 0){
                    productRows.html(' ')
                    i = data.products.length
                    $.each(data.products, function(index, value){
                      console.log(value)
                      var newCartItemRemove = hiddenCartItemRemoveForm.clone()
                      newCartItemRemove.css("display", "block")
                      // newCartItemRemove.removeClass("hidden-class")
                      newCartItemRemove.find(".cart-item-product-id").val(value.id)
                        cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + "<h5>" + value.name + "</h5>" + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
                        i --
                    })
                    
                    cartBody.find(".cart-tax").text("8.4%")
                    cartBody.find(".cart-subtotal").text(data.subtotal)
                    cartBody.find(".cart-total").text(data.total)
                } else {
                  window.location.href = currentUrl
                }
                
              },
              error: function(errorData){
                console.log("error")
                console.log(errorData)
              }
            })


          }

      })


















