#!/usr/bin/env bash

scalac -cp scalatest_2.9.0-1.8.jar hw4/*.scala
#scala -cp scalatest_2.9.0-1.8.jar org.scalatest.run TestTree
scala Parser "2.0 * 3.0 / 4.0"
scala Parser "2.0 / 3.0 * 4.0"
