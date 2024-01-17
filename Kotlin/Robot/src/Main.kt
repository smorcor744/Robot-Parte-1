/**
 * 1ºCrear una versión del programa ¿Dónde está R2D2?, pero ORIENTADO A OBJETOS.
 *
 * 2ºLa clase Robot debe tener 4 propiedades: nombre, posX, posY y direccion. También tendrá un comportamiento por medio de 3 métodos: mover(), mostrarPosicion() y obtenerDireccion().
 *
 * 3ºEl método mover() debe recibir un array de elementos enteros y no retornará nada, ya que los cambios quedarán almacenados en las propiedades del mismo.
 *
 * 4ºEl método obtenerDireccion() no recibe parámetros y retorna una cadena de caracteres con la dirección PositiveX, NegativeX, PositiveY o NegativeY. (Posible mejora con class enum https://kotlinlang.org/docs/enum-classes.html)
 *
 * 5ºEl método mostrarPosicion() debe mostrar por consola la posición y dirección. Ejemplo: R2D2 está en (10, -5) PositiveX.
 *
 * 6ºUn objeto de la clase Robot debe inicializarse siempre en la posición (0, 0) y la dirección eje Y positivo (hacia arriba) cuando se instancia. En esta versión ya no va a moverse siempre desde la posición (0,0), sino que lo hará desde la última posición y dirección dónde se quedó al realizar su último movimiento.
 *
 * 7ºEn este programa, vamos a realizar los mismos movimientos, pero el robot comenzará cada movimiento en la posición final después de realizar el movimiento anterior.
 *
 * 8ºEn el main debes crear un objeto de Robot (o una variable de tipo Robot) con el nombre R2D2. El nombre de la variable que utilices para crearlo puede ser robot1.
 *
 * 9ºLa clase Robot debe obligar a introducir un nombre que no esté vacío.
 *
 * 10ºCread los movimientos en un array de arrays y recorrerlos para realizar en cada iteración los movimientos del robot y mostrar la posición del mismo al finalizar cada uno. En cada iteración del bucle llamaremos a los métodos mover() y mostrarPosicion().
 * [
 *     [1, -5, 0, -9],
 *     [3, 3, 5, 6, 1, 0, 0, -7],
 *     [2, 1, 0, -1, 1, 1, -4],
 *     [],
 *     [3, 5]
 *
 * */
/**
 * Clase Robot que representa un robot en un plano 2D.
 *
 * @property nombre El nombre del robot.
 * @property posX La posición del robot en el eje X.
 * @property posY La posición del robot en el eje Y.
 * @property dir La dirección en la que se mueve el robot.
 */
class Robot(private val nombre:String ){
    var posX : Int = 0
    var posY : Int = 0
    var dir : Int = 0

    /**
     * Método para mover al robot.
     *
     * @param movimientos Un array de enteros que representan los movimientos del robot.
     */
    fun mover(movimientos: IntArray) {
        for (pasos in movimientos ) {
            when (this.dir){
                0 -> this.posY += pasos
                1 -> this.posX -= pasos
                2 -> this.posY -= pasos
                3 -> this.posX += pasos
            }
            if (this.dir == 3) this.dir = 0 else this.dir++
        }
    }
    //Enumeracion de las direcciónes
    enum class direc {POSITIVEY,NEGATIVEX,NEGATIVEY,POSITIVEX}
    /**
     * Método para obtener la dirección del robot.
     *
     * @return Una cadena de caracteres que representa la dirección del robot.
     */
    private fun obtenerDireccion() = when (this.dir){
        0 -> direc.POSITIVEY
        1 -> direc.NEGATIVEX
        2 -> direc.NEGATIVEY
        3 -> direc.POSITIVEX
        else -> {""}
    }

    /**
     * Método para mostrar la posición y dirección del robot.
     */
    fun mostrarPosocion(){
        println("${this.nombre} está en (${this.posX}, ${this.posY}) ${this.obtenerDireccion()}")
    }
}

/**
 * Método principal del programa.
 */
fun main() {
    // Creación de un objeto de la clase Robot
    val robot1 = Robot("R2D2")

    // Definición de los movimientos del robot
    val movimientos = arrayOf(
        intArrayOf(1, -5, 0, -9),
        intArrayOf(3, 3, 5, 6, 1, 0, 0, -7),
        intArrayOf(2, 1, 0, -1, 1, 1, -4),
        intArrayOf(), intArrayOf(3, 5))

    // Bucle para realizar los movimientos del robot y mostrar su posición
    for (movimiento in movimientos){
        robot1.mover(movimiento)
        robot1.mostrarPosocion()
    }
}
