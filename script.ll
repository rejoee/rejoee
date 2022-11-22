<script>
    x = 50
    y = 350
    xi = 1
    yi = 0
    setInterval(()=>{
        x += xi
        y += yi
        if (x>950 || x<50) xi = -xi
        if (y>650 || y<50) yi = -yi
        yi += 0.01
        document.getElementById("x").setAttribute("cx", x)
        document.getElementById("x").setAttribute("cy", y)

    },1)
    function g(e) {
        document.getElementById("f").setAttribute("cx", e.x)
    }
       <script>
         div {
  background-color: red;
  border-radius: 100%;
  height: 50px;
  left: calc(50% - 50px);
  position: absolute;
  right: calc(50% - 50px);
  width: 50px;
  animation: bounce 1s ease-in-out infinite;
  animation-fill-mode: both;
  animation-direction: alternate;
}

span {
  border-radius: 100%;
  bottom: 32.5%;
  left: calc(50% - 50px);
  right: calc(50% - 50px);
  position: absolute;
  content: '';
  background-color: black;
  filter: blur(3px);
  width: 50px;
  height: 5px;
  animation: shadow 1s ease-in-out infinite;
  animation-fill-mode: both;
  animation-direction: alternate;
  z-index: -1;
}

@keyframes bounce {
  from {
    top: 25%;
    transform: scaleX(79.5%) scaleY(65%);
  }
  to {
    top: 55%;
  }
}


@keyframes shadow {
  from {
    opacity: 0;
    transform: scale(0);
  }
  to {
    opacity: .5;
    transform: scale(100%);
  }
}
</script>
</html>
