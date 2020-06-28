package com.sairam.myapp

import java.io.FileWriter
import java.io.IOException
import java.util.*

/*
* Code to create csv file with kotlin
*/

class Customer {
    var id: String? = null
    var name: String? = null
    var address: String? = null
    var age: Int = 0

    constructor() {}
    constructor(id: String?, name: String?, address: String?, age: Int) {
        this.id = id
        this.name = name
        this.address = address
        this.age = age
    }

    override fun toString(): String {
        return "Customer [id=" + id + ", name=" + name + ", address=" + address + ", age=" + age + "]"
    }
}

private val CSV_HEADER = "id,name,address,age"

fun createCsv() {

    val customers = Arrays.asList(
        Customer("1", "Jack Smith", "Massachusetts", 23),
        Customer("2", "Adam Johnson", "New York", 27),
        Customer("3", "Katherin Carter", "Washington DC", 26),
        Customer("4", "Jack London", "Nevada", 33),
        Customer("5", "Jason Bourne", "California", 36))

    var fileWriter: FileWriter? = null

    try {
        fileWriter = FileWriter("customer.csv")

        fileWriter.append(CSV_HEADER)
        fileWriter.append('\n')

        for (customer in customers) {
            fileWriter.append(customer.id)
            fileWriter.append(',')
            fileWriter.append(customer.name)
            fileWriter.append(',')
            fileWriter.append(customer.address)
            fileWriter.append(',')
            fileWriter.append(customer.age.toString())
            fileWriter.append('\n')
        }

        println("Write CSV successfully!")
    } catch (e: Exception) {
        println("Writing CSV error!")
        e.printStackTrace()
    } finally {
        try {
            fileWriter!!.flush()
            fileWriter.close()
        } catch (e: IOException) {
            println("Flushing/closing error!")
            e.printStackTrace()
        }
    }
}