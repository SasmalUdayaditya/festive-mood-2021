package com.sp.hack.models;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Student {
    @Id
    private long stdId;
    private String name;
    private String address;

    public Student() {
    }

    public Student(long stdId, String name, String address) {
        this.stdId = stdId;
        this.name = name;
        this.address = address;
    }

    public long getStdId() {
        return stdId;
    }

    public void setStdId(long stdId) {
        this.stdId = stdId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
