function validate()
      {
      
         if( document.username_form.username.value.length < 4 )
         {
            alert( "Username has to be longer than 4 characters!" );
            document.username_form.cookbook_name.focus() ;
            return false;
         }
         return( true );
      }
      