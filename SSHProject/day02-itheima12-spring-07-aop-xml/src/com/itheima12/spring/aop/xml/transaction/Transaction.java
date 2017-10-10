package com.itheima12.spring.aop.xml.transaction;

import java.lang.reflect.Method;

import org.junit.Test;




//切面
public class Transaction {
	public void beginTransaction(){
		System.out.println("begin transaction");
	}
	
	public void commit(){
		System.out.println("commit");
	}
	@Test
	public void testMethod() {
		Class class1=Object.class;
	   Method[] me=class1.getMethods();
		for (Method m:me) {
			System.out.println(me.toString());
		}
		
	}
}
