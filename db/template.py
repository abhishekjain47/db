<form action="/success/" method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Submit" />
</form>