<%inherit file="base.mako"/>

<form action="" method="POST">
   <div class="form-group">
      % for field in form:
         <label for="${field.id}">
            ${ field.label() }
         </label>
         ${ field(class_="form-control") }
      % endfor
   </div>

   <input value="Speichern" type="submit" />
</form>
