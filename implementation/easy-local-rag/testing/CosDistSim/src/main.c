#include "raylib.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

#define MAX_POINTS 300

typedef struct {
    char label[32];
    Vector3 position;
    float color;
} DataPoint;

DataPoint points[MAX_POINTS];
int pointCount = 0;

void LoadData(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Failed to open file!\n");
        return;
    }
    
    char buffer[1024];
    fgets(buffer, sizeof(buffer), file); // Read labels
    
    char labels[MAX_POINTS][32];
    float x[MAX_POINTS], y[MAX_POINTS], z[MAX_POINTS], c[MAX_POINTS];
    
    sscanf(buffer, "Labels: [%[^]]]", buffer);
    char *token = strtok(buffer, " ,'");
    int index = 0;
    while (token && index < MAX_POINTS) {
        strncpy(labels[index++], token, 31);
        token = strtok(NULL, " ,'");
    }
    
    pointCount = 0;
    fscanf(file, "X: [%[^]]]", buffer);
    token = strtok(buffer, " ,");
    while (token && pointCount < MAX_POINTS) {
        x[pointCount++] = atof(token);
        token = strtok(NULL, " ,");
    }
    
    pointCount = 0;
    fscanf(file, " Y: [%[^]]]", buffer);
    token = strtok(buffer, " ,");
    while (token) {
        y[pointCount++] = atof(token);
        token = strtok(NULL, " ,");
    }
    
    pointCount = 0;
    fscanf(file, " Z: [%[^]]]", buffer);
    token = strtok(buffer, " ,");
    while (token) {
        z[pointCount++] = atof(token);
        token = strtok(NULL, " ,");
    }
    
    pointCount = 0;
    fscanf(file, " C: [%[^]]]", buffer);
    token = strtok(buffer, " ,");
    while (token) {
        c[pointCount++] = atof(token);
        token = strtok(NULL, " ,");
    }
    
    fclose(file);
    
    for (int i = 0; i < pointCount; i++) {
        strncpy(points[i].label, labels[i], 31);
        points[i].position = (Vector3){ x[i], y[i], z[i] };
        points[i].color = c[i];
    }
}

int main() {
    InitWindow(800, 600, "3D Scatter Plot");
    Camera3D camera = { 0 };
    camera.position = (Vector3){ 10.0f, 10.0f, 10.0f };
    camera.target = (Vector3){ 0.0f, 0.0f, 0.0f };
    camera.up = (Vector3){ 0.0f, 1.0f, 0.0f };
    camera.fovy = 45.0f;
    camera.projection = CAMERA_PERSPECTIVE;
    SetTargetFPS(60);
    
    LoadData("data.txt");
    
    while (!WindowShouldClose()) {
        UpdateCamera(&camera, CAMERA_ORBITAL);
        
        BeginDrawing();
        ClearBackground(RAYWHITE);
        
        BeginMode3D(camera);

        float maxcolor = 1.0f;
        float mincolor = 0.0f;
        for (int i = 0; i < pointCount; i++) {
            maxcolor = fmax(maxcolor, points[i].color); // Find maximum color
			mincolor = fmin(mincolor, points[i].color);
        }

        for (int i = 0; i < pointCount; i++) {
			float normalizedColor = (int)(0 + (points[i].color - mincolor) * (0 + 32) / (maxcolor - mincolor));
			Color color = ColorFromHSV(normalizedColor, 1.0f, 1.0f);
            DrawSphere(points[i].position, 0.2f, color);
        }

        DrawGrid(10, 1.0f);
        EndMode3D();
        
        for (int i = 0; i < pointCount; i++) {
            Vector2 screenPos = GetWorldToScreen(points[i].position, camera);
            DrawText(points[i].label, (int)screenPos.x, (int)screenPos.y, 20, BLACK);
        }
        
        DrawText("Use mouse to rotate view", 10, 10, 20, DARKGRAY);
        EndDrawing();
    }
    
    CloseWindow();
    return 0;
}
