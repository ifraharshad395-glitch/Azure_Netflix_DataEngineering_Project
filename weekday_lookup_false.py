# Databricks notebook source
var = dbutils.jobs.taskValues.get(taskKey='Weekday_lookup', key='weekoutput')

# COMMAND ----------

print(var)